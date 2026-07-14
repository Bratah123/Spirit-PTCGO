from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card


def _dragon_discard_attacks(ctx):
    pairs = []
    seen = set()
    for card in ctx.discard_pile():
        if not is_pokemon_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.DRAGON.value not in types:
            continue
        definition = def_for(card.archetype_id)
        if definition is None:
            continue
        for ability in getattr(definition, "abilities", []):
            if isinstance(ability, Attack):
                key = (ability.title, ability.game_text)
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((card, ability))
    return pairs


async def apex_dragon(ctx):
    """Choose an attack from a Dragon Pokemon in your discard pile and use
    it as this attack."""
    candidates = _dragon_discard_attacks(ctx)
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


async def legacy_star(ctx):
    """VSTAR Power: you may discard the top 7 of your deck, then put up to
    2 cards from your discard pile into your hand."""
    if await ctx.ask_yes_no("Discard the top 7 cards of your deck?"):
        top = ctx.deck_top(7)
        if top:
            await ctx.discard_cards(top)
    picks = await ctx.choose_cards(
        ctx.discard_pile(), 2, minimum=0,
        prompt="Put up to 2 cards from your discard pile into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="dc29d870-7d97-58cb-9baf-6185bd8733af",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegidragoVSTAR.Name",
    display_name="Regidrago VSTAR",
    searchable_by=["Regidrago VSTAR", "VSTAR", "RegidragoVSTAR"],
    subtypes=["VSTAR"],
    collector_number=201,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RegidragoV.Name",
    family_id=895,
    abilities=[
        Ability(
            title="Legacy Star",
            game_text="During your turn, you may discard the top 7 cards of your deck. Then, put up to 2 cards from your discard pile into your hand. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=legacy_star,
        ),
        Attack(
            title="Apex Dragon",
            game_text="Choose an attack from a Dragon Pok\u00e9mon in your discard pile and use it as this attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.FIRE: 1},
            effect=apex_dragon,
        ),
    ],
)
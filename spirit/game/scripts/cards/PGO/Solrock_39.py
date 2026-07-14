from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType

LUNATONE_NAME = "com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name"


def _is_psychic_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value \
        and PokemonTypes.PSYCHIC.value in types


def _my_lunatones(pokemon_list):
    return [p for p in pokemon_list
            if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == LUNATONE_NAME]


def sun_energy_condition(board, player_id, pokemon):
    if not _my_lunatones(board.pokemon_in_play(player_id)):
        return False
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_is_psychic_energy_card(c) for c in discard.children)


async def sun_energy(ctx):
    lunatones = _my_lunatones(ctx.my_pokemon_in_play())
    cards = [c for c in ctx.discard_pile() if _is_psychic_energy_card(c)]
    if not lunatones or not cards:
        return
    if not await ctx.ask_yes_no(
        "Attach a Psychic Energy card from your discard pile to 1 of your Lunatone?"
    ):
        return
    picks = await ctx.choose_cards(cards, 1, prompt="Choose a Psychic Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        lunatones, "Choose a Lunatone to attach the Energy to"
    ) or lunatones[0]
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="2470d314-35d8-54be-b8c4-3f0f504f0765",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Sun Energy",
            game_text="Once during your turn, you may attach a Psychic Energy card from your discard pile to 1 of your Lunatone.",
            activation=Activations.ONCE_PER_TURN,
            condition=sun_energy_condition,
            effect=sun_energy,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
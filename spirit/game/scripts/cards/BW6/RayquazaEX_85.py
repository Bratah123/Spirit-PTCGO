from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.trainers import is_basic_energy_card


async def celestial_roar(ctx):
    """Discard the top 3 cards of your deck; attach any Energy among them."""
    top = ctx.deck_top(3)
    await ctx.discard_cards(top)
    for card in top:
        if is_energy_card(card):
            await ctx.attach_energy(card, ctx.source)


async def _dragon_burst(ctx):
    """Discard all basic Fire or all basic Lightning Energy attached to this
    Pokemon; 60 damage times the number of Energy discarded."""
    def of_type(t):
        return [e for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e)
                and t.value in (e.get_attribute(AttrID.POKEMON_TYPES) or [])]
    fire, lightning = of_type(PokemonTypes.FIRE), of_type(PokemonTypes.LIGHTNING)
    chosen = fire or lightning
    if fire and lightning:
        index = await ctx.choose("Discard which Energy?", ["Fire", "Lightning"])
        chosen = fire if index == 0 else lightning
    if not chosen:
        return
    await ctx.discard_cards(chosen)
    await ctx.deal_damage(60 * len(chosen))


card = PokemonCardDef(
    guid="2593d077-a5d4-57ac-93ba-c4178ffcb790",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=85,
    set_code="BW6",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=384,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=celestial_roar,
        ),
        Attack(
            title="Dragon Burst",
            game_text="Discard all basic Fire Energy or all basic Lightning Energy attached to this Pok\u00e9mon. This attack does 60 damage times the number of Energy you discarded.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=_dragon_burst,
        ),
    ],
)
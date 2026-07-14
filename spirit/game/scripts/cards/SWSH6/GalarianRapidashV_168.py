from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def libra_horn(ctx):
    """Put damage counters on 1 of the opponent's Pokemon until its
    remaining HP is 100."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    current = target.get_attribute(AttrID.HP, ctx.max_hp(target))
    if current > 100:
        await ctx.deal_damage(current - 100, target=target, apply_modifiers=False,
                              as_counters=True)


card = PokemonCardDef(
    guid="4251601d-8c27-583a-bc6e-2d5ce97f7c6a",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRapidashV.Name",
    display_name="Galarian Rapidash V",
    searchable_by=["Galarian Rapidash V", "Basic", "V", "GalarianRapidashV"],
    subtypes=["Basic", "V"],
    collector_number=168,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=78,
    abilities=[
        Attack(
            title="Libra Horn",
            game_text="Put damage counters on 1 of your opponent's Pok\u00e9mon until its remaining HP is 100.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=libra_horn,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=60),
        ),
    ],
)
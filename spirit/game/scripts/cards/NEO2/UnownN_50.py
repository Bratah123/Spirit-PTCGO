from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_type_reduce_passive


card = PokemonCardDef(
    guid="b14fcdaf-506f-5a28-8090-11c2d26c7b02",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownN.Name",
    display_name="Unown [N]",
    searchable_by=["Unown [N]", "Basic", "UnownN"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Normal]",
            game_text="Whenever a Colorless Pok\u00e9mon damages 1 of your Pok\u00e9mon, reduce that damage by 30 (after applying Weakness and Resistance). This power stops working if you have more than 1 Unown [N] in play. (This power works even if Unown [N] is Asleep, Confused, or Paralyzed.)",
            ability_type=AbilityTypes.POKE_POWER,
            passive=unown_type_reduce_passive(PokemonTypes.COLORLESS, "N"),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)

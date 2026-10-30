from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_type_reduce_passive


card = PokemonCardDef(
    guid="ead0b44f-2829-5134-a745-5e20fc34c96c",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownD.Name",
    display_name="Unown [D]",
    searchable_by=["Unown [D]", "Basic", "UnownD"],
    subtypes=["Basic"],
    collector_number=47,
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
            title="[Darkness]",
            game_text="Whenever a Darkness Pok\u00e9mon damages 1 of your Pok\u00e9mon, reduce that damage by 30 (after applying Weakness and Resistance). This power stops working if you have more than 1 Unown [D] in play. (This power works even if Unown [D] is Asleep, Confused, or Paralyzed.)",
            ability_type=AbilityTypes.POKE_POWER,
            passive=unown_type_reduce_passive(PokemonTypes.DARKNESS, "D"),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)

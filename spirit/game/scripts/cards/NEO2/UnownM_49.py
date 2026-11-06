from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_type_reduce_passive


card = PokemonCardDef(
    guid="5b29ac3d-5a9c-5ea3-bb59-882a8f133b16",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownM.Name",
    display_name="Unown [M]",
    searchable_by=["Unown [M]", "Basic", "UnownM"],
    subtypes=["Basic"],
    collector_number=49,
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
            title="[Metal]",
            game_text="Whenever a Metal Pok\u00e9mon damages 1 of your Pok\u00e9mon, reduce that damage by 30 (after applying Weakness and Resistance). This power stops working if you have more than 1 Unown [M] in play. (This power works even if Unown [M] is Asleep, Confused, or Paralyzed.)",
            ability_type=AbilityTypes.POKE_POWER,
            passive=unown_type_reduce_passive(PokemonTypes.METAL, "M"),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)

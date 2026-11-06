from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import same_attached_energy_count


card = PokemonCardDef(
    guid="fc36d270-d772-53db-8732-d4e3435c31b3",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasAbra.Name",
    display_name="Sabrina's Abra",
    searchable_by=["Sabrina's Abra", "Basic", "SabrinasAbra"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Synchronize",
            game_text="This attack can't be used unless Sabrina's Abra and the Defending Pok\u00e9mon have the same number of Energy cards attached to them.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            condition=same_attached_energy_count,
        ),
    ],
)

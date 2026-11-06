from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage


card = PokemonCardDef(
    guid="0e797485-d5c0-5805-a2c2-f8e488965d8e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Baby", "Smoochum"],
    subtypes=["Baby"],
    collector_number=61,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=238,
    abilities=[
        Attack(
            title="Energy Kiss",
            game_text="Flip a number of coins equal to the number of Energy cards attached to the Defending Pok\u00e9mon. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(
                coins_from=count_energy("defender", cards=True),
                per_heads=10,
            ),
        ),
    ],
)

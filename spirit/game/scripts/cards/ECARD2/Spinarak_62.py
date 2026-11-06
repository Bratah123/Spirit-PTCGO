from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="8dd1d1d8-df81-59fe-96d6-1f54bd2c7652",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak", "Basic", "Spinarak"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=167,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Gooey Thread",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)

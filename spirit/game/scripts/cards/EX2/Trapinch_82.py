from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="8872e525-e2c3-58f9-a0cf-7a56f424607c",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Sand Pit",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Irongrip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)

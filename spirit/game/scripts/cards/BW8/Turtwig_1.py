from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="2bf9d224-1619-5578-ba44-490ebfd9f6b6",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=387,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(20),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
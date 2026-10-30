from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import cant_attack_next_turn


card = PokemonCardDef(
    guid="106a76dd-496c-5dc7-893f-1345b87f93b1",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Lazy Punch",
            game_text="Slakoth can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=cant_attack_next_turn(),
        ),
    ],
)

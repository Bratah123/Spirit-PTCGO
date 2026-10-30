from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import increased_base_damage_next_turn


card = PokemonCardDef(
    guid="996ef45a-67f7-564b-8d15-748abbad3ecf",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    display_name="Vigoroth",
    searchable_by=["Vigoroth", "Stage 1", "Vigoroth"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    family_id=287,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, base damage of Vigoroth's Slash is attack is 90 instead of 40.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=increased_base_damage_next_turn(("Slash", 50)),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)

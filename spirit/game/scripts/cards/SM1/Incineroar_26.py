from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="c6b2a4ff-a602-540b-9fdf-ee401183f0ab",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name",
    display_name="Incineroar",
    searchable_by=["Incineroar", "Stage 2", "Incineroar"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Darkest Lariat",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=100),
        ),
    ],
)
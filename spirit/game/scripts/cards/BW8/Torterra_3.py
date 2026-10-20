from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="7885dfe2-543a-59b4-a1a2-916797df2828",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name",
    display_name="Torterra",
    searchable_by=["Torterra", "Stage 2", "Team Plasma", "Torterra"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=3,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, any damage to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Rumble Stomp",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)
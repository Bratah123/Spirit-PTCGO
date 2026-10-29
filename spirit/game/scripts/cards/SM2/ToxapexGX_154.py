from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import flip_damage, condition_attack
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="ddcbabc7-30f1-5179-99bd-59868e9ce036",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxapexGX.Name",
    display_name="Toxapex-GX",
    searchable_by=["Toxapex-GX", "Stage 1", "GX", "ToxapexGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=154,
    set_code="SM2",
    rarity=Rarities.RareRainbow,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    family_id=747,
    abilities=[
        Attack(
            title="Spike Cannon",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(4, per_heads=30),
        ),
        Attack(
            title="Super Intense Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 10 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=condition_attack(SpecialConditions.POISONED, counters=10, damage=0),
        ),
        Attack(
            title="Total Shelter-GX",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=150,
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)
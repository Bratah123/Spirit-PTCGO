from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage

card = PokemonCardDef(
    guid="80f18789-1d99-5768-9806-a6684539280e",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Rapid Strike", "Carnivine"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=9,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=455,
    abilities=[
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Triple Whip",
            game_text="Flip 3 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=60),
        ),
    ],
)

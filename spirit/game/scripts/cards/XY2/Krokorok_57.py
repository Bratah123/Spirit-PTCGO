from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="f2e74081-81e1-5ab7-8b18-1478e6a162ae",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1", "Krokorok"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Dark Clamp",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Double Swing",
            game_text="Flip 2 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=60),
        ),
    ],
)
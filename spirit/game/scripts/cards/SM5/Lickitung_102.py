from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="02ed82af-c64a-5066-87de-4d52c99d0fd2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Lap Up",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=draw_attack(3),
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)
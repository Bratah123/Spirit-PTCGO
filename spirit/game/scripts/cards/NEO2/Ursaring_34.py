from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing, flip_damage


card = PokemonCardDef(
    guid="c078bffb-e8c7-582d-b20b-1ecd532fd2a6",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Headpress",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=flip_or_nothing(then=condition_attack(SpecialConditions.PARALYZED)),
        ),
        Attack(
            title="Double Lariat",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=40),
        ),
    ],
)

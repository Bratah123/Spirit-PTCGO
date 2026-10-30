from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="4827f4e9-162c-56c0-a147-5eef63337b2f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMachoke.Name",
    display_name="Giovanni's Machoke",
    searchable_by=["Giovanni's Machoke", "Stage 1", "GiovannisMachoke"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMachop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Risky Attack",
            game_text="Flip a coin. If tails, this attack does no damage to the Defending Pok\u00e9mon and Giovanni's Machoke does 100 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=flip_damage(require_all=True, tails_self_damage=100),
        ),
        Attack(
            title="Headlock",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage and the Defending Pok\u00e9mon is now Paralyzed. If tails, this attack does 20 damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True, heads_bonus_damage=20,
            ),
        ),
    ],
)

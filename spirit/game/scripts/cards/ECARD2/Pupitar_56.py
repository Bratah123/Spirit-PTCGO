from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="7b6762a2-2048-53cc-b7d9-5ac09a7841f0",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage. If tails, Pupitar does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_damage(bonus=10, tails_self_damage=10),
        ),
    ],
)

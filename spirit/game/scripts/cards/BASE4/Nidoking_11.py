from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="c2b13595-105d-5fff-a2ce-53dec7986080",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage; if tails, this attack does 30 damage and Nidoking does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(bonus=10, require_all=True, tails_self_damage=10),
        ),
        Attack(
            title="Toxic",
            game_text="The Defending Pok\u00e9mon is now Poisoned. It now takes 20 Poison damage instead of 10 after each player's turn (even if it was already Poisoned).",
            cost={PokemonTypes.GRASS: 3},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
    ],
)

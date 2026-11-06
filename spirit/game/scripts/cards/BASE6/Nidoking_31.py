from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="e4babb1e-32cd-537c-b4e3-e81583da0103",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="BASE6",
    rarity=Rarities.Rare,
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

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="873706d0-4ec7-5f20-9dca-cd37b8871e16",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    display_name="Piloswine",
    searchable_by=["Piloswine", "Stage 1", "Piloswine"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Nap",
            game_text="Remove 3 damage counters from Piloswine. If it has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=heal_attack(30),
        ),
        Attack(
            title="High-Speed Charge",
            game_text="Piloswine does 30 damage to itself. Piloswine can't use this attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            locks_next_turn=True,
            effect=recoil_attack(30),
        ),
    ],
)

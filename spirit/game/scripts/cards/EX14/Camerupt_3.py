from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import delta_protection_vs_delta
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="eed763d3-0b92-59d9-93e2-f1e0360ad2ef",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1", "Camerupt"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Delta Protection",
            game_text="Any damage done to Camerupt by attacks from your opponent's Pok\u00e9mon that has \u03b4 on its card is reduced by 40 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=delta_protection_vs_delta(),
            effect=None,
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(30, pool='any'),
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
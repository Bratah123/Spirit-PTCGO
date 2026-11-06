from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import sneak_attack


card = PokemonCardDef(
    guid="ae12f2fd-7fb0-597f-bf54-f2b3b4d1dc35",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolbat.Name",
    display_name="Dark Golbat",
    searchable_by=["Dark Golbat", "Stage 1", "DarkGolbat"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Sneak Attack",
            game_text="When you play Dark Golbat from your hand, you may choose 1 of your opponent's Pok\u00e9mon. If you do, Dark Golbat does 10 damage to that Pok\u00e9mon. Apply Weakness and Resistance.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=sneak_attack,
        ),
        Attack(
            title="Flitter",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.GRASS: 2},
            effect=snipe_attack(
                20, pool="any", apply_modifiers=False,
                prompt="Choose 1 of your opponent's Pokémon"),
        ),
    ],
)

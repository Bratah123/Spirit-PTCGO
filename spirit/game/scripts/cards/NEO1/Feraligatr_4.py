from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_counters_on, flip_damage
from spirit.game.card_effects.ecard import berserk


card = PokemonCardDef(
    guid="1491ffc0-426d-5360-9dff-4fc550e3e49e",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Berserk",
            game_text="When you play Feraligatr from your hand, flip a coin. If heads, discard the top 5 cards from your opponent's deck. If tails, discard the top 5 cards from your deck.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=berserk,
        ),
        Attack(
            title="Chomp",
            game_text="Flip a number of coins equal to the number of damage counters on Feraligatr. This attack does 50 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.WATER: 4},
            damage=50,
            damage_operator="+",
            effect=flip_damage(bonus_per_heads=10, coins_from=damage_counters_on("self")),
        ),
    ],
)

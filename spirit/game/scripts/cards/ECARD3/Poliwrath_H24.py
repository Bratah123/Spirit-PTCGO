from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import strange_spiral, strange_spiral_condition


card = PokemonCardDef(
    guid="fccab15a-4dc4-5b22-8485-a8e84f561bdf",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=174,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Strange Spiral",
            game_text="Once during your turn (before your attack), if Poliwrath is your Active Pok\u00e9mon, you may discard a basic Energy card attached to Poliwrath. If you do, the Defending Pok\u00e9mon is now Confused. This power can't be used if Poliwrath is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=strange_spiral_condition,
            effect=strange_spiral,
        ),
        Attack(
            title="Spiral Punch",
            game_text="Flip a coin until you get tails. This attack does 40 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import mega_throw, spiral_confused_no_retreat


card = PokemonCardDef(
    guid="e98db418-dec3-57de-9566-b4ed6b3f2292",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Spiral",
            game_text="As long as Poliwrath is your Active Pok\u00e9mon, your opponent's Confused Pok\u00e9mon can't retreat.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=spiral_confused_no_retreat(),
        ),
        Attack(
            title="Split Spiral Punch",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Mega Throw",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=mega_throw(50, 30),
        ),
    ],
)
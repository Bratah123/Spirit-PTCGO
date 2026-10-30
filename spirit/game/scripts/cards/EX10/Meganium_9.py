"""STUB: effect not implemented — do not guess mechanics.
Meganium (EX10 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import healing_aroma_between_turns, bouncy_move

card = PokemonCardDef(
    guid="d58f4338-0a5c-5384-9dda-40e08e1d8893",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Healing Aroma",
            game_text="As long as Meganium is your Active Pok\u00e9mon, remove 1 damage counter from each Pok\u00e9mon (excluding Pok\u00e9mon-ex) (both yours and your opponent's) between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=healing_aroma_between_turns(1),
        ),
        Attack(
            title="Bouncy Move",
            game_text="You may put up to 5 damage counters on Meganium. If you do, this attack does 50 damage plus 10 more damage for each damage counter you put on Meganium in this way.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bouncy_move(50, 10, 5),
        ),
    ],
)
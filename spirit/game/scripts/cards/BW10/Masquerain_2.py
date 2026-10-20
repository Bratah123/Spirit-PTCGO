from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b309100b-2846-5fa2-ad95-e60d102f1cb2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Team Plasma", "Masquerain"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=2,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Ability(
            title="Tool Reversal",
            game_text="As often as you like during your turn (before your attack), you may put a Pok\u00e9mon Tool card attached to 1 of your Pok\u00e9mon into your hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
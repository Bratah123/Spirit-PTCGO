from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.data_utils import subtypes_for


card = PokemonCardDef(
    guid="d255a8d7-52d7-5c93-b36e-918cf47db138",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1", "Golisopod"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Ability(
            title="Armor",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Resolute Claws",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-GX or a Pok\u00e9mon-EX, this attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and ('GX' in subtypes_for(ctx.defender.archetype_id) or 'EX' in subtypes_for(ctx.defender.archetype_id)), 70),
        ),
    ],
)
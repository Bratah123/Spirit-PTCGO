from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import DarkAuraPassive, stamp


card = PokemonCardDef(
    guid="473fa3c8-4ff2-5843-9e68-4b531ccca224",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Dark Aura",
            game_text="All Energy attached to Tyranitar is Darkness Energy instead of its usual type.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=DarkAuraPassive(),
        ),
        Attack(
            title="Stamp",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 10 more damage and does 10 damage to each of your opponent's Benched Pok\u00e9mon, if any. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 4},
            damage=50,
            damage_operator="+",
            effect=stamp,
        ),
    ],
)

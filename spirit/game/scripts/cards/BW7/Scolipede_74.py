from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fb64b174-f355-5033-9fd0-544b65ab8076",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name",
    display_name="Scolipede",
    searchable_by=["Scolipede", "Stage 2", "Scolipede"],
    subtypes=["Stage 2"],
    collector_number=74,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    family_id=543,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), this Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Venoshock",
            game_text="If the Defending Pok\u00e9mon is Poisoned, this attack does 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
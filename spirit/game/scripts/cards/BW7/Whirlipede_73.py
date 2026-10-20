from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="411757c7-ae55-5567-8471-7a63a4c32da0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    display_name="Whirlipede",
    searchable_by=["Whirlipede", "Stage 1", "Whirlipede"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    family_id=543,
    abilities=[
        Ability(
            title="Poison Point",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), this Attacking Pok\u00e9mon is now Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
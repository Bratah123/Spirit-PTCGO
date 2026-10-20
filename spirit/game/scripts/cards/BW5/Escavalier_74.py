from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a70b62e-2d2e-5903-8e07-025ef1f46eb8",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1", "Escavalier"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard a Pok\u00e9mon Tool card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Cavalry Lance",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)
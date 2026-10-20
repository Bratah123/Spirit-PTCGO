from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28c68674-f7ec-5dba-8713-16ca77214fc8",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Gather Order",
            game_text="Search your deck for as many Combee as you like and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Damage Beat",
            game_text="Does 20 damage times the number of damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
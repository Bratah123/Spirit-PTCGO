from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b051e86-b75e-56fe-a5a5-025197121682",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Destructive Sound",
            game_text="Your opponent reveals his or her hand. Discard all Item cards you find there.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
        Attack(
            title="Round",
            game_text="Does 50 damage times the number of your Pok\u00e9mon that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
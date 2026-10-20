from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8615af42-d009-50c3-9a47-11ad919be95b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=97,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Strong Breeze",
            game_text="Your opponent shuffles the Defending Pok\u00e9mon and all cards attached to it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=unimplemented,
        ),
    ],
)
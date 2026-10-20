from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5333328-1b93-5991-b322-dcff8161defb",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2", "Team Plasma", "Krookodile"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=70,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Piston Headbutt",
            game_text="Move an Energy attached to the Defending Pok\u00e9mon to 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
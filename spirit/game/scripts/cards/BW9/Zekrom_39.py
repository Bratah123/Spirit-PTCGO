from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5e8dcfdd-a932-5965-bc71-2baf1edbbea8",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Fusion Bolt",
            game_text="If Reshiram is on your Bench, this attack does 40 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
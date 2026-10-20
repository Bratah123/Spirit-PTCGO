from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="89512d3d-21db-5b04-b399-09e370804201",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZekromEX.Name",
    display_name="Zekrom-EX",
    searchable_by=["Zekrom-EX", "Basic", "EX", "ZekromEX"],
    subtypes=["Basic", "EX"],
    collector_number=51,
    set_code="BW4",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Glinting Claw",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Strong Volt",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)
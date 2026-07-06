from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22aa9879-2682-505a-8f4c-5cf215e93d80",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WyrdeerV.Name",
    display_name="Wyrdeer V",
    searchable_by=["Wyrdeer V", "Basic", "V", "WyrdeerV"],
    subtypes=["Basic", "V"],
    collector_number=180,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=899,
    abilities=[
        Ability(
            title="Frontier Road",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may move any amount of Energy from your other Pok\u00e9mon to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Psyshield Bash",
            game_text="This attack does 40 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
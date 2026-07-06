from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="41075035-7467-53a6-95bd-1bdf7862570c",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMoltresV.Name",
    display_name="Galarian Moltres V",
    searchable_by=["Galarian Moltres V", "Basic", "V", "GalarianMoltresV"],
    subtypes=["Basic", "V"],
    collector_number=176,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=146,
    abilities=[
        Ability(
            title="Direflame Wings",
            game_text="Once during your turn, you may attach a Darkness Energy card from your discard pile to this Pok\u00e9mon. You can't use more than 1 Direflame Wings Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Aura Burn",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)
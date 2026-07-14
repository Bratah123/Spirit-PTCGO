from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import debuff_defender_attacks

card = PokemonCardDef(
    guid="ba60ffbe-a51d-57b9-895c-59bd2947ed2b",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonV.Name",
    display_name="Duraludon V",
    searchable_by=["Duraludon V", "Basic", "V", "Single Strike", "DuraludonV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=198,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=884,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=70,
        ),
        Attack(
            title="Breaking Swipe",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2},
            damage=140,
            effect=debuff_defender_attacks(30),
        ),
    ],
)
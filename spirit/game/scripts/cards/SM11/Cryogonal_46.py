from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import distort


card = PokemonCardDef(
    guid="19acd55d-b34c-590e-9f60-821f630b27a8",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Cryogonal"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Frozen Lock",
            game_text="Your opponent can't play any Item cards from their hand during their next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=distort,
        ),
    ],
)
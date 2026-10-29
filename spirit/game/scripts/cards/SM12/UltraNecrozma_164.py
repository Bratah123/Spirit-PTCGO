from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import ultra_burst_passive
from spirit.game.card_effects.pokemon import rock_crush


card = PokemonCardDef(
    guid="5b28e8c3-8f98-589a-8c88-d7f4871047c1",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozma.Name",
    display_name="Ultra Necrozma",
    searchable_by=["Ultra Necrozma", "Basic", "Ultra Beast", "UltraNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=164,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=800,
    abilities=[
        Ability(
            title="Ultra Burst",
            game_text="This Pok\u00e9mon can't attack unless your opponent has 2 or fewer Prize cards remaining.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=ultra_burst_passive,
        ),
        Attack(
            title="Luster of Downfall",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=170,
            effect=rock_crush,
        ),
    ],
)
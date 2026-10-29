from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import altered_creation_gx
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="dc6d7c4f-53cc-5b05-b12b-e6f637b29e29",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusDialgaPalkiaGX.Name",
    display_name="Arceus & Dialga & Palkia-GX",
    searchable_by=["Arceus & Dialga & Palkia-GX", "Basic", "TAG TEAM", "GX", "ArceusDialgaPalkiaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=258,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=483,
    abilities=[
        Attack(
            title="Ultimate Ray",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=search_attach_energy(predicate=is_basic_energy_card, count=3, distribute=True),
        ),
        Attack(
            title="Altered Creation-GX",
            game_text="For the rest of this game, your Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance). If this Pok\u00e9mon has at least 1 extra Water Energy attached to it (in addition to this attack's cost), when your opponent's Active Pok\u00e9mon is Knocked Out by damage from those attacks, take 1 more Prize card. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=altered_creation_gx,
        ),
    ],
)
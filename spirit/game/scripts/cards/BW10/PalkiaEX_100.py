from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="33eaa38d-f7dd-52fa-a91c-5e1c7e384799",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaEX.Name",
    display_name="Palkia-EX",
    searchable_by=["Palkia-EX", "Basic", "EX", "Team Plasma", "PalkiaEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=100,
    set_code="BW10",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    family_id=484,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Dimension Heal",
            game_text="Heal from this Pok\u00e9mon 20 damage for each Plasma Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)
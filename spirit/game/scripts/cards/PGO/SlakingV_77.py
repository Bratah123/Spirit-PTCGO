from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _prizes_remaining(board, player_id):
    area = board.find_player_area(player_id, "prizePile")
    return len(area.children) if area else 0


def _kinda_lazy_condition(board, player_id, pokemon):
    return _prizes_remaining(board, player_id) not in (2, 4, 6)


card = PokemonCardDef(
    guid="2fa3076d-77d0-50cb-afb3-6c3c81cbdc46",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlakingV.Name",
    display_name="Slaking V",
    searchable_by=["Slaking V", "Basic", "V", "SlakingV"],
    subtypes=["Basic", "V"],
    collector_number=77,
    set_code="PGO",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=289,
    abilities=[
        Ability(
            title="Kinda Lazy",
            game_text="If you have exactly 2, 4, or 6 Prize cards remaining, this Pok\u00e9mon can't attack.",
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.COLORLESS: 4},
            damage=260,
            condition=_kinda_lazy_condition,
        ),
    ],
)
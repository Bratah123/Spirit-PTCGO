from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.models.board import PokemonEntity, PlayerEntity


def _opponent_has_pokemon_v(pokemon, carrier):
    root = carrier
    while root.parent is not None:
        root = root.parent
    for player in root.children:
        if not isinstance(player, PlayerEntity):
            continue
        if player.owning_player_id == carrier.owning_player_id:
            continue
        for area in player.children:
            for card in getattr(area, "children", []):
                if isinstance(card, PokemonEntity) and is_pokemon_v(card.archetype_id):
                    return True
    return False


card = PokemonCardDef(
    guid="b9e39666-3332-5c20-89e8-e460ed95c0b0",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=767,
    abilities=[
        Ability(
            title="Punk Out",
            game_text="If your opponent has any Pokémon V in play, this Pokémon has no Retreat Cost.",
            passive=retreat_free_when(_opponent_has_pokemon_v),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot


class PrimalLawPassive(Passive):
    def blocks_evolution(self, player_id, target, carrier):
        return player_id != carrier.owning_player_id and is_in_active_spot(carrier)


card = PokemonCardDef(
    guid="ca58be7f-9ced-5aad-93ec-fcce58b975b8",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dracovish.Name",
    display_name="Dracovish",
    searchable_by=["Dracovish", "Stage 1", "Dracovish"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=882,
    abilities=[
        Ability(
            title="Primal Law",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Pok\u00e9mon from their hand to evolve their Pok\u00e9mon.",
            passive=PrimalLawPassive(),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
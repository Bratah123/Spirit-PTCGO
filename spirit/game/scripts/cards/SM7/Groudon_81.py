from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.sm7 import (
    wreck,
)


card = PokemonCardDef(
    guid="f3d0db98-f55a-5c6b-8823-81bc7f392cbd",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Wreck",
            game_text="If there is any Stadium card in play, this attack does 50 more damage. Then, discard that Stadium card.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=wreck,
        ),
        Attack(
            title="Ground Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
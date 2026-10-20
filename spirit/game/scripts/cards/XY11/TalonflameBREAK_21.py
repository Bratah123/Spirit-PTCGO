from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="078d4ad4-5dd0-5174-87b0-7a6be0b234b8",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TalonflameBREAK.Name",
    display_name="Talonflame BREAK",
    searchable_by=["Talonflame BREAK", "BREAK", "TalonflameBREAK"],
    subtypes=["BREAK"],
    collector_number=21,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=150,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
    ],
)